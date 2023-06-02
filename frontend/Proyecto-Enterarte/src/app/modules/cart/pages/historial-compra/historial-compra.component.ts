import { Component, OnInit} from '@angular/core';
import { HistorialCompraService } from 'src/app/services/historial-compra.service';


@Component({
  selector: 'app-historial-compra',
  templateUrl: './historial-compra.component.html',
  styleUrls: ['./historial-compra.component.css']
})
export class HistorialCompraComponent implements OnInit{
  public historialA: any =[];
  mostrarHistorial:boolean=true;

  constructor(private historialS: HistorialCompraService){

  }
  
  ngOnInit(): void {
    this.historialS.mostrarHistorial()
    .subscribe( resp =>{ 
      this.historialA = resp;
    });
    
    
  } 
}