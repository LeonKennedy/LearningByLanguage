/**
 * Created by olenji on 19/7/17.
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 */
public class AddTwoNumer {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }
    public static void main(String[] args){
        ListNode l12 = new ListNode(4);
        l12.next = new ListNode(3);
        ListNode l11 = new ListNode(2);
        l11.next = l12;
        ListNode l22 = new ListNode(6);
        l22.next = new ListNode(4);
        ListNode l21 = new ListNode(5);
        l21.next = l22;

        AddTwoNumer atn = new AddTwoNumer();
        ListNode ld = atn.addTwoNumbers(l11, l21);

        while(ld!= null){
            System.out.println(ld.val);
            ld = ld.next;
        }

    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}