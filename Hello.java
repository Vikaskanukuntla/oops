class Computer {

    int age;
    String val;

    Computer(int age , String val){
        this.age = age;
        this.val = val;
    }

     void config(){
        System.out.println("etc etc" + age + "val" + val);
    }
}

public class Hello{
    public static void main(String[] args) {
        Computer comp1 = new Computer(21 , "12x");
        comp1.config();
    }
}