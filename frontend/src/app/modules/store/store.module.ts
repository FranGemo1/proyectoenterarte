import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StoreRoutingModule } from './store-routing.module';
import { StoreComponent } from './pages/store/store.component';
import { ProductListComponent } from './components/product-list/product-list.component';
import { ProductDetailComponent } from './components/product-detail/product-detail.component';
import { ProductItemComponent } from './components/product-item/product-item.component';
import { CartComponent } from './pages/cart/cart.component';
import { FdepagosComponent } from './pages/fdepagos/fdepagos.component';

@NgModule({
  declarations: [
    ProductListComponent,
    ProductDetailComponent,
    ProductItemComponent,
    StoreComponent,
    CartComponent,
    FdepagosComponent
  ],
  exports: [StoreRoutingModule],
  imports: [CommonModule],
})
export class StoreModule {}
