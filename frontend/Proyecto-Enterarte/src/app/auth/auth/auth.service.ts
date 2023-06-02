import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor() {}
  login(username: string, password: string): boolean {
    // Lógica de autenticación aquí
    // Devuelve true si las credenciales son válidas, false de lo contrario
    return true;
  }

  register(username: string, password: string): boolean {
    // se comprueba si las credenciales son válidas

    if (this.validateUsername(username) && this.validatePassword(password)) {
      // Lógica adicional para registrar al usuario
      console.log('Registro exitoso');
      return true;
    } else {
      // Mostrar mensajes de error o realizar acciones adicionales
      console.log('Registro fallido');
      return false;
    }
  }

  private validateUsername(username: string): boolean {
    // Lógica para validar el nombre de usuario
    return username.length > 6;
  }

  private validatePassword(password: string): boolean {
    // Lógica para validar la contraseña
    return password.length > 8;
  }
}
