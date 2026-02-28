public static void main(String[] args) {
    int edad= 18;
    boolean tieneCarnet= true;
    if (edad >= 18 && tieneCarnet) {
        System.out.println("Puedes ir a la fiesta con tus amigos.");
    } else if (edad < 18 && !tieneCarnet) {
        System.out.println("primero debes ser mayor de edad para tener un carnet.");
    } else if (edad >= 18 && !tieneCarnet) {
        System.out.println("primero debes obtener tu carnet para ir a la fiesta.");
    } else {
        System.out.println("No puedes ir a la fiesta con tus amigos.");
    }
}
    