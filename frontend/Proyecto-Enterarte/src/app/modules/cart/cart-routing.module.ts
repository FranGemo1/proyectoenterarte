import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CartComponent } from './pages/cart/cart.component';
import { FdepagosComponent } from './pages/fdepagos/fdepagos.component';
import { HistorialCompraComponent } from './pages/historial-compra/historial-compra.component';



const routes: Routes = [
  {path:'',
  component: CartComponent
  },
  {path:'pagos',
  component: FdepagosComponent
  },
  {path:'historial',
  component: HistorialCompraComponent
  }
  
];

  @NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
  })

export class CartRoutingModule { }
