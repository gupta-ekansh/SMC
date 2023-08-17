#include <iostream>
#include <lzo/lzo1z.h>

using namespace std;

int main() {
    char compressed_data[4096];  // Adjust buffer size as needed
    char decompressed_data[4096];  // Adjust buffer size as needed

    // Read compressed data from standard input
    cin.read(compressed_data, sizeof(compressed_data));
    int compressed_size = cin.gcount();

    // Decompress using lzo1z algorithm
    lzo_uint in_len = sizeof(decompressed_data);
    int decompressed_size = sizeof(decompressed_data);

    int result = lzo1z_decompress(reinterpret_cast<const lzo_bytep>(compressed_data),
                                  static_cast<lzo_uint>(compressed_size),
                                  reinterpret_cast<lzo_bytep>(decompressed_data),
                                  &in_len,
                                  NULL);

    if (result == LZO_E_OK) {
        // Print decompressed data to standard output
        cout.write(decompressed_data, in_len);
    } else {
        cerr << "Decompression error" << endl;
        return 1;
    }

    return 0;
}