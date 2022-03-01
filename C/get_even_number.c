// Print even number from n to m

#include<stdio.h>

int main()
{
    int m,n,x=0;
    
    // #01
    n=1,m=10;
    for (n;n<=m;++n)
    {
        if(n%2==0)
        {
            printf("%d\n",n);
        }

    }

    // #01_02
    n=1,m=10;
    while(n<=m)
    {
        if(n%2==0)
        {
            printf("%d\n",n);
        }
        ++n;
    }

    
    // #02
    // without mod (learnt from ohi sir 
    // (thou its widely avialable at web)

    n=1,m=10;
    for (n; n<=m; ++n)
    {
        if((n/2)*2==n)
        {
            printf("%d\n",n);
        }

    }

    
    // #03
    // my 2nd approach after failing at first 
    // approach and learning few core concepts of maths (-,-)

    n=1,m=10;
    for (n; n<=m; ++n)
    {
        x = n;
        while(x>=2)
        {
            x -=2;
        }
        if (!x)
        {
            printf("%d\n",n);
        }
    }

    // #03_02
    n=1,m=10;
    while(n<=m)
    {
        x = n;
        while(x>=2)
        {
            x-=2;
        }

        if (!x)
        {
            printf("%d\n",n);
        }
        ++n;
    }


    // #04
    // using bitwise operator
    // ref. http://www.xcprod.com/titan/XCSB-DOC/binary_and.html
    //      https://www.tutorialspoint.com/cprogramming/c_bitwise_operators.htm

    n=1,m=10;
    while(n<=m)
    {
        if (!(n & 1))
        {
            printf("%d\n",n);
        }
        ++n;
    }

    return 0;
}
