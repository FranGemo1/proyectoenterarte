import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class HomeService {
  private items: string[] = ['Item 1', 'Item 2', 'Item 3'];

  constructor() {}
  getItems(): string[] {
    // Retorna los items disponibles
    return this.items;
  }

  addItem(item: string): void {
    // Agrega un nuevo item a la lista
    this.items.push(item);
  }

  removeItem(index: number): void {
    // Remueve un item de la lista basado en su índice
    if (index >= 0 && index < this.items.length) {
      this.items.splice(index, 1);
    }
  }
}
