package aula001;
public class bola {
  
   
       String cor;
       float circun;
       String material;

       public bola(String cor, float circun, String material){
        this.cor=cor;
        this.circun=circun;
        this.material=material;
       }

       public String getTrocarCor(){
           return cor;
       }
       public void setTrocarCor(String setTrocarCor){
           this.cor = setTrocarCor;
       }
   }
