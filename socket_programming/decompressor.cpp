#include <sys/types.h>
#include <iostream>
#include <stdlib.h>

#define bswap_16(x) _byteswap_ushort(x)
#define bswap_32(x) _byteswap_ulong(x)
#define bswap_64(x) _byteswap_uint64(x)

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <chrono>

#include "MulticastHeader.h"
#include <lzo/lzo1z.h>

int main() {
    // Compressed data
    const char* compressed_data = "\x00\xce\x1a\x02..."; // Your compressed data here
    size_t compressed_size = sizeof(compressed_data);

    // Initialize LZO
    if (lzo_init() != LZO_E_OK) {
        // Handle initialization error
        return 1;
    }

    // Allocate memory for the decompressed data
    size_t max_decompressed_size = compressed_size * 4; // A rough estimate, you can adjust this as needed
    lzo_bytep out_buf = (lzo_bytep)malloc(max_decompressed_size);
    if (out_buf == nullptr) {
        // Handle memory allocation error
        return 1;
    }

    lzo_uint out_len;

    // Perform decompression
    int ret = lzo1z_decompress_safe((const lzo_bytep)compressed_data, compressed_size, out_buf, &out_len, nullptr);
    if (ret != LZO_E_OK) {
        // Handle decompression error
        free(out_buf);
        return 1;
    }

    // Use the decompressed data in 'out_buf'

    // Clean up
    free(out_buf);
    return 0;
}
