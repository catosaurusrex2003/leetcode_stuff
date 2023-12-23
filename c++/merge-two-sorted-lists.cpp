/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        if (list1 == NULL)
            return list2;
        if (list2 == NULL)
            return list1;

        ListNode *finalHead = list1;
        if (list1->val > list2->val)
        {
            finalHead = list2;
            cout << "adding " << list2->val << " from 2";
            list2 = list2->next;
        }
        else
        {
            cout << "adding " << list1->val << " from 1";
            list1 = list1->next;
        }

        ListNode *curr = finalHead;
        while (list1 && list2)
        {
            if (list1->val < list2->val)
            {
                curr->next = list1;
                cout << "adding " << list1->val << " from 1";
                list1 = list1->next;
            }
            else
            {
                curr->next = list2;
                cout << "adding " << list2->val << " from 2";
                list2 = list2->next;
            }
            curr = curr -> next;
        }
        if (list1)
        {
            cout << "adding rest " << list1->val << " from 1";
            curr->next = list1;
        }
        else
        {
            cout << "adding rest " << list2->val << " from 2";
            curr->next = list2;
        }

        return finalHead;
    }
};