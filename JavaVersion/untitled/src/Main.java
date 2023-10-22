class A
{
    private int a = 10;
    private int count = 0;
    public A(int a)
    {
        this.a = a;
    }
    public A()
    {
        if (count == 0){
            this.a = 20;
        }
        else {
            this.a = 30;
        }
        count++;
    }
    public void display()
    {
        System.out.println("a=" + a);
    }
}

class B extends A
{
    public B(int a)
    {
        super.display();
    }

    public void B1(int b)
    {
        super();
        super.display();
    }
}


public class Main
{
    public static void main(String[] args)
    {
        B obj = new B(10);
        obj.B1(20);
    }
}