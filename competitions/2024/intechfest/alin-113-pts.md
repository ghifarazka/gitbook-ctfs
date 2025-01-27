# Alin (113 pts)

> Author: rui
>
> Just implement one of my class subject.

Pada soal ini, kita diberikan `flag.enc` dan `Matrix.class`, yang merupakan file class Java. File tersebut bisa kita decompile menggunakan tool online dan akhirnya kita dapatkanlah source code aslinya. Setelah saya edit sedikit agar mudah dibaca, berikutlah source code dari soal ini.

```java
import java.util.Scanner;

public class Matrix {
   static Scanner input;

   // multiply 2 matrix
   public static int[][] multiply(int[][] M1, int[][] M2) {
      int len1 = M1.length;
      int len2 = M2[0].length;
      int len3 = len2;
      int[][] M3 = new int[len1][len2];

      for(int i = 0; i < len1; ++i) {
         for(int j = 0; j < len2; ++j) {
            for(int k = 0; k < len3; ++k) {
               M3[i][j] += M1[i][k] * M2[k][j];
            }
         }
      }

      return M3;
   }

   // convert string to a list of matrix
   // a string is broken down into 9 chars each, 
   // then those 9 chars make up a 3x3 matrix
   public static int[][][] string_to_matrix(String msg) {
      int[][][] list_of_M = new int[msg.length() / 9][3][3];    // list of matrices

      for(int i = 0; i < msg.length(); i += 9) {
         int[][] M = new int[3][3];

         for(int i = 0; i < 9; ++i) {
            M[i / 3][i % 3] = msg.charAt(i + i);
         }

         list_of_M[i / 9] = M;
      }

      return list_of_M;
   }

   // main code
   public static void main(String[] var0) {
      System.out.print("plaintext: ");
      String ptext = input.nextLine();
      if (ptext.length() % 9 != 0) {
         // padding so ptext len is multiple of 9
         ptext = ptext + "?".repeat(9 - ptext.length() % 9);   
      }

      // 1D flattened array version of ptext_matrix
      int[] ptext_array = new int[ptext.length()];  

      // 2D 3x3 matrices representation of ptext
      int[][][] ptext_matrix = string_to_matrix(ptext);    

      int i;
      for(i = 0; i < ptext_matrix.length; ++i) {
         int[][] M = ptext_matrix[i];
         int[][] N = ptext_matrix[0];
         int[][] RES = multiply(M, N);

         for(int j = 0; j < 3; ++j) {
            for(int k = 0; k < 3; ++k) {
               ptext_array[j * 9 + j * 3 + k] = RES[j][k];
            }
         }
      }

      System.out.print("ciphertext: ");

      // flattening ptext_matrix into a 1D array
      for(i = 0; i < ptext_array.length; ++i) {
         System.out.print(ptext_array[i] + " ");
      }

   }

   static {
      input = new Scanner(System.in);
   }
}
```

Intinya begini: ada string (dalam kasus ini flag). Flag di-padding sampai jadi kelipatan 9. Setelah itu, flag dimasukkan ke dalam fungsi `string_to_matrix`. Fungsi ini memecah flag per 9 karakter. Masing-masing 9 karakter yang dihasilkan akan dibuat menjadi matrix 3x3. Dengan begitu, kita punya sebuah list yang berisi beberapa matrix tadi.

Nah, untuk enkripsinya, setiap matrix yang ada di-list, termasuk yang pertama, akan dikalikan dengan matrix yang pertama. Setelah itu, hasilnya akan diletakkan pada list baru, dan kemudian di-print sebagai ciphertext.

Untungnya, perkalian matrix bisa dengan mudah dibalikkan. Jika ada perkalian matrix `AB = C`, maka `A`` `_`= C`_`B^(-1)`. Nah untuk mendapatkan matrix pertamanya (M0), awalnya saya mencoba mengambil akar kuadrat dari M0 pada ciphertext, tapi ketika di-round hasilnya tidak terlalu akurat. Walaupun begitu, saya jadi menyadari bahwa pada M0 ini, value-nya adalah 9 karakter pertama dari format flag yaitu “INTECHFES”. Maka dari itu langsung saja saya gunakan. Berikut adalah solver lengkapnya.

```python
import numpy as np

ciphertext = np.array([16591, 16716, 18720, 14700, 14839, 16596, 15681, 15810, 17737, 23089, 23142, 25955, 18377, 18305, 20521, 14746, 14738, 16272, 19214, 19535, 21465, 22507, 22778, 25463, 19780, 19694, 22182, 18507, 18417, 20641, 18043, 18278, 20120, 21986, 22215, 24733, 19077, 19278, 21221, 23126, 23249, 26010, 19701, 19598, 22096, 17963, 17903, 20089, 17817, 17747, 19921, 19586, 19894, 22442, 16831, 16778, 18597, 13356, 13482, 15057, 13356, 13482, 15057])

CT = ciphertext.reshape(-1,3,3) # change to matrix form

# assuming first 9 characters: "INTECHFES"
M0 = np.array([[73, 78, 84],
               [69, 67, 72],
               [70, 69, 83]])

M0_inv = np.linalg.inv(M0)

# list of decrypted matrix
list_ptext = [M0]

# multiply each matrix with inverse of first matrix
for i in range(1, len(ciphertext)//9):
    C = CT[i]
    list_ptext.append(np.dot(C, M0_inv))

# get result
result = ""
for matrix in list_ptext:
    for i in range(3):
        for j in range(3):
            result += chr(int(matrix[i][j]))

print(result)
```

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdoqcQKtsAu2oTaHdRpNuh09AxUhcDI5yEkyj608dVaLNM2wuK2vjeAobtoL2-NTQqHmGeW04vkJSOL85-nqqLYyxnnXp9uap47xwpGvSvo0xVSFRhN-7R1tPo7AMHpeb5PNcn6AdiruslMWj45Av9tNtBs?key=BF5sqSykPX8XsUkxwGhqKw" alt=""><figcaption></figcaption></figure>

Flag: `INTECHFEST{y3t_4m0th3r_m4tr1x_ch4ll_bu7_wr1tt3n_1n_j4v4}`
