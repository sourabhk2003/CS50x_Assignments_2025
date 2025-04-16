#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#define BLOCK_SIZE = 512
int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Error occurred in opening the raw file.\n")
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
           fwrite(&buffer, 1, 512, );

    }
}
