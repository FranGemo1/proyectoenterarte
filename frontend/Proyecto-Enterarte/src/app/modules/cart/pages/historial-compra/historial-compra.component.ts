import { Component } from '@angular/core';


@Component({
  selector: 'app-historial-compra',
  templateUrl: './historial-compra.component.html',
  styleUrls: ['./historial-compra.component.css']
})
export class HistorialCompraComponent {
  today=new Date();
  HistorialCompra:boolean=true;
  Historial=[{evento:"Cuentos que no son cuentos", monto:"500", date:"d/M/yy", hora:""},{evento:"Cuentos que si son cuentos", monto:"600", date:"d/M/yy", hora:""},{evento:"Artes Visuales", monto:"700", date:"d/M/yy", hora:""},{evento:"Cuentos que si son cuentos", monto:"600", date:"d/M/yy", hora:""},{evento:"Musica 2023", monto:"750", date:"d/M/yy", hora:""}];
  
  constructor(){}

}
