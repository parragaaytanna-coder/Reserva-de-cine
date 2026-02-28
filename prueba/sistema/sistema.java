package prueba.sistema;

public class sistema {
    public static void main(String[] args) {
        boolean sistemaActivo= true;
        boolean tienePermiso= true;
        if (sistemaActivo==true) {
            if (tienePermiso==true) {
                System.out.println("Accion ejecutada");
            } else {
                System.out.println("Permiso denegado");
            }
        } else {
            System.out.println("Sistema inactivo");
        }
    }
    
}
