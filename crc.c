#include <stdio.h>
#include <string.h>

void xorOperation(char dividend[], char divisor[], int key_len) {
    for (int i = 0; i < key_len; i++)
        dividend[i] = (dividend[i] == divisor[i]) ? '0' : '1';
}

void mod2div(char dividend[], char divisor[], int data_len, int key_len) {
    int i, j;
    for (i = 0; i <= data_len - key_len + 1; i++) {
        if (dividend[i] == '1') {
            xorOperation(&dividend[i], divisor, key_len);
        }
    }
}

void encodeData(char data[], char key[], char encoded[]) {
    int data_len = strlen(data), key_len = strlen(key);
    char temp[50];

    strcpy(temp, data);
    for (int i = 0; i < key_len - 1; i++)
        strcat(temp, "0");

    mod2div(temp, key, data_len + key_len - 1, key_len);

    strcpy(encoded, data);
    strcat(encoded, temp + data_len);
}

int main() {
    char data[50], key[20], encoded[50];

    printf("Enter data: ");
    scanf("%s", data);
    printf("Enter divisor: ");
    scanf("%s", key);

    encodeData(data, key, encoded);
    printf("Encoded Data: %s\n", encoded);

    return 0;
}
