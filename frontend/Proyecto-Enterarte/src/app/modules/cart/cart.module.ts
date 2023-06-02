import { Component, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CartRoutingModule } from './cart-routing.module';
import { CartComponent } from './pages/cart/cart.component';
import { FdepagosComponent } from './pages/fdepagos/fdepagos.component';
import { HistorialCompraComponent } from './pages/historial-compra/historial-compra.component';






@NgModule({
  declarations: [
    CartComponent,FdepagosComponent,HistorialCompraComponent
      ],
  imports: [
    CommonModule,
   CartRoutingModule
    
  ],
  
  
})
export class CartModule { }
