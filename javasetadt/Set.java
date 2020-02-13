
public class Set{
   private LinkedNode head;

   public Set(){
      head = null;
   }
 
   public void add(int x){
	   if(!exists(x))
		   head = new LinkedNode(x, head);
   }

 
 
   public String toString(){
      StringBuffer result = new StringBuffer();
      LinkedNode tmp = head;
      while(tmp != null) {
      	result.append(tmp.data + " ");
      	tmp = tmp.next;
      }

      return result.toString();
   }
   
   public boolean exists(int x)
   {
	  LinkedNode tmp = head;
      while(tmp != null) {
         if(tmp.data == x) return true;
         tmp = tmp.next;
      }

      return false;
   }

   public void delete(int x){
      if(head == null)
    	  	return;

      if( head.data == x ){
         head = head.next;
         return;
      }

      LinkedNode cur  = head;
      LinkedNode prev = null;

      while(cur != null && cur.data != x){
         prev = cur;
         cur = cur.next;
      }

      if(cur == null)
    	  	return;

      //delete cur node
      if(prev != null)
    	  	prev.next = cur.next;
   }

   

}
