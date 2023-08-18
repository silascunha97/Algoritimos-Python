package aula001;
public class main {
    public static void main(String[] args){
    bola b1 = new bola("Verde", 3.7f, "plastico");
    System.out.println(b1.getTrocarCor());
    b1.setTrocarCor("Azul");
    System.out.println(b1.getTrocarCor());
    }
}
