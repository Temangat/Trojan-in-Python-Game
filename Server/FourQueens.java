interface Printable {
    void print();   // abstract
     default void honk() { //default method
        System.out.println("Beep beep!");
    }
}
class Invoice implements Printable {
    public void print() {
        System.out.println("Invoice printed.");
    }
}

interface A { void showA(); }
interface B { void showB(); }

class C implements A, B {
    public void showA() { System.out.println("A"); }
    public void showB() { System.out.println("B"); }
}
