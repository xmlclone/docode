#include <stdio.h>
#include <string.h>

void encrypt(char* data, char* key) {
    int data_length = strlen(data);
    int key_length = strlen(key);
    
    for (int i = 0; i < data_length; i++) {
        data[i] = data[i] ^ key[i % key_length];
    }
}

void decrypt(char* data, char* key) {
    int data_length = strlen(data);
    int key_length = strlen(key);
    
    for (int i = 0; i < data_length; i++) {
        data[i] = data[i] ^ key[i % key_length];
    }
}

// int main() {
//     char key[] = "mysecretkey";
//     char plaintext[] = "Hello World!";
    
//     // 加密明文
//     xor_encrypt_decrypt(plaintext, key);
//     printf("Encrypted text: %s\n", plaintext);
    
//     // 解密密文
//     xor_encrypt_decrypt(plaintext, key);
//     printf("Decrypted text: %s\n", plaintext);
    
//     return 0;
// }