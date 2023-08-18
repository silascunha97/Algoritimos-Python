package Caneta;

public class Caneta {
  public String modelo;
  public String cor;
  private float ponta;
  protected int carga;
  protected boolean tampada;

   public void status(){
      System.out.println("Uma caneta é " + this.cor);
      System.out.println("Está tampada " + this.tampada);
      System.out.println("Está o modelo é " + this.modelo);
      System.out.println("Está a ponta está " + this.ponta);
   }

   public Caneta( String modelo, String cor, float getTrocaPonta, int getTrocaCarga){
      this.cor = cor;
      this.modelo = modelo;
      this.ponta = getTrocaPonta;
      this.carga = getTrocaCarga;
   }

   public void rabiscar(){
      if(this.tampada == true){
        System.out.println("Erro! não é possivel rabiscar."); 
      }else{
         System.out.println("Estou rabiscando "); 
      }
   }

   public float setTrocaPonta(){
      return this.ponta;
   }
   public void getTrocaPonta(float getTrocaPonta){
      this.ponta = ponta;
   }
   public float setTrocaCarga(){
      return this.carga;
   }
   public void getTrocaCarga(float getTrocacarga){
      this.carga = carga;
   }

   protected void tampar(){
      this.tampada = true;
   }

   protected void destampar(){
    this.tampada = false;
   }
}
