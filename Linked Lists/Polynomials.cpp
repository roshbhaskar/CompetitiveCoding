/*

Given two polynomial numbers represented by a linked list. 
Write a function that add these lists means add the coefficients who have same variable powers.

struct Node {
    int coeff;
    int pow;
    struct Node* next;
};

*/

#include <iostream>
using namespace std;

struct ExprTerm{
    double coeff;
    double power;
    struct ExprTerm * next;
};

void addPoly(struct ExprTerm* expr1,struct ExprTerm* expr2,struct ExprTerm*result)
{
    while(expr1->next && expr2->next)
    {
        if(expr1->power > expr2->power)
        {
            result->power=expr1->power;
            result->coeff = expr1->coeff;
            expr1=expr1->next;
        }
        else if(expr1->power < expr2->power)
        {
            result->power=expr2->power;
            result->coeff = expr2->coeff;
            expr1=expr2->next;
        }
        else //if(expr1->power == expr2->power)
        {
            result->power=expr1->power;
            result->coeff = expr1->coeff + expr2->coeff;
            expr1=expr1->next;
            expr2=expr2->next;
        }
        result->next = (struct ExprTerm*)malloc(sizeof(struct ExprTerm));
        result=result->next;
        result->next=NULL;
    }
    
    //if any terms are leftover
    while(expr1->next || expr2->next)
    {
        if(expr1->next)
        {
            result->power = expr1->power;
            result->coeff = expr1->coeff;
            expr1=expr1->next;
        }
        if(expr2->next)
        {
            result->power = expr2->power;
            result->coeff = expr2->coeff;
            expr2=expr2->next;
        }
        result->next = (struct ExprTerm*)malloc(sizeof(struct ExprTerm));
        result=result->next;
        result->next=NULL;
        
    }
    
}
