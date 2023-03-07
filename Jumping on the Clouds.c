#include<stdio.h>
#include<math.h>
 
int main(int argc, char const *argv[])
{
	int n,i,count=0;
	scanf("%d",&n);
	int arr[n];

	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}

	for(i=0;i<n-1;i++)
	{
		if(arr[i+2]==0)
		{
			count++;
			i=i+1;
		}

		else
			count++;
	}

	printf("%d\n",count);
	return 0;
}
     
