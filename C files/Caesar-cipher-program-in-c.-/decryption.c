#include<stdio.h> 
#include<conio.h> 
#include<string.h>
#include<ctype.h> 
void main()
{       int i, key; 
      char text[100],c; 
   
      printf("\nCaesar Cipher- Decryption");    
 printf("\nEnter Message To Decrypt : ");     
 gets(text);       
 printf("\nEnter Key : ");   
 scanf("%d", &key); 
  for(i = 0; text[i] != '\0'; ++i) 
      {      
    c = text[i];  
    if(c >= 'a' && c <= 'z') 
      {    
      c = c - key; 
       if(c < 'a') 
       { 
      c = c + 'z' - 'a' + 1; 
      }    
      text[i] = c; 
      } 
      else if(c >= 'A' && c <= 'Z') 
      {       c = c - key;    
       if(c < 'A')   
      { 
      c = c + 'Z' - 'A' + 1; 
      }     
       text[i] = c; 
      } 
      } 
      printf("Decrypted text: %s", text); 
      getch(); 
} 
