#include <bits/stdc++.h>
using namespace std;

int n, cnt = 1, flag1[100], flag2[100], flag3[100], res[100];
// Biến n là số quân hậu, cnt là đếm số trường hợp(dùng để in kết quả), 3 mảng flag đánh dấu chưa xuất hiện lần lượt ở cột, đường chéo xuôi, đường chéo ngược và mảng res để lưu kết quả.
void setup()
{
    for (int i = 1; i <= 2*n + 1; i++)
    {
        flag1[i] = 1;
        flag2[i] = 1;
        flag3[i] = 1;
    }
}
// Hàm setup đánh dấu tất cả giá trị bằng 1, tức là chưa xuất hiện ở cột, đường chéo xuôi, đường chéo ngược.

void Result()
{
    cout << "TH" << cnt++ << ": ";
    for (int i = 1; i < n; i++)
        cout << "(" << i << ", " << res[i] << ");  ";
    cout << "(" << n << ", " << res[n] << ")\n";
}
// Hàm Result để in kết quả cho mỗi trường hợp.

void Try(int i)
{
    for (int j = 1; j <= n; j++)
    {
        if (flag1[j] && flag2[i - j + n] && flag3[i + j - 1])
        {
            res[i] = j;
            flag1[j] = 0;
            flag2[i - j + n] = 0;
            flag3[i + j - 1] = 0;
            if (i == n)
                Result();
            else
                Try(i+1);         
            flag1[j] = 1;
            flag2[i - j + n] = 1;
            flag3[i + j - 1] = 1;
        }
    }
}
// Quay lui có điều kiện.

int main()
{
    cout << "Nhap so quan hau: ";
    cin >> n;
    setup();
    cout << "Vi tri cac quan hau:" << endl;
    Try(1);
    return 0;
}