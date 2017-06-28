//This is a c code that will insert image to remote PostgreSQL database using decryption 
#include <libpq-fe.h>
#include <stdlib.h>
#include <arpa/inet.h>

static void
exit_nicely(PGconn *conn)
{
    PQfinish(conn);
    exit(1);
}

PGresult* put_data_to_Images(
  PGconn* conn,
  int id,
  int data_size,
  const char* const data
) {
  PGresult* result;
  const unsigned int id_big_endian = htonl((unsigned int)id);
  const char* const paramValues[] = { &id_big_endian, data };
  const int nParams = sizeof(paramValues) / sizeof(paramValues[0]);
  const int paramLenghts[] = { sizeof(id_big_endian), data_size };
  const int paramFormats[] = { 1, 1 }; /* binary */
  const int resultFormat = 0; /* text */

  result = PQexecParams(
    conn,
    "insert into Images (id, data) values ($1::integer, $2::bytea)",
    nParams,
    NULL, /* Types of parameters, unused as casts will define types */
    paramValues,
    paramLenghts,
    paramFormats,
    resultFormat
  );
  return result;
}

int main(int argc, char** argv)
{
	char conninfo[30];
/*	if(argc < 3)
	{
		printf("Usage: ./pgbin 192.168.50.12 postgres im1.png\n");
		return -1;
	}*/
	sprintf(conninfo, "dbname=postgres hostaddr=192.168.50.12 user=postgres password=faban sslmode=disable");//, argv[2], argv[1]);
	PGconn* conn = PQconnectdb(conninfo);
	char *bytes;
	if (PQstatus(conn) != CONNECTION_OK)
    	{
        	printf("Connection to database failed: %s",
                	PQerrorMessage(conn));
        	exit_nicely(conn);
    	}
//	FILE* fptr = fopen(argv[3], "rb");
	FILE* fptr = fopen("im1.png", "rb");
	if(!fptr)
	{
		printf("Couldn't open image file %s.\n", argv[3]);
		return -2;
	}
	//Get file length
	fseek(fptr, 0, SEEK_END);
	int fileLen=ftell(fptr);
	fseek(fptr, 0, SEEK_SET);

	//Allocate memory
	bytes=(char *)malloc(fileLen+10);
	if (!bytes)
	{
		printf("Memory error!\n");
                fclose(fptr);
		return -3;
	}

	//Read file contents into buffer
	fread(bytes, fileLen, 1, fptr);
	fclose(fptr);


	PGresult* res = put_data_to_Images(conn, 0, fileLen, bytes);
	PQclear(res);
	PQfinish(conn);
	free(bytes);
	return 0;
}
