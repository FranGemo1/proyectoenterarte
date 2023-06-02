import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/header/header.component';
import { FooterComponent } from './shared/footer/footer.component';
import { AboutModule } from './modules/about/about.module';
import { AuthModule } from './modules/auth/auth.module';
import { CartModule } from './modules/cart/cart.module';
import { CreateEventModule } from './modules/create-event/create-event.module';
import { Error404Module } from './modules/error404/error404.module';
import { EventsModule } from './modules/events/events.module';
import { HomeModule } from './modules/home/home.module';
import { ProfileUserModule } from './modules/profile-user/profile-user.module';
import { HttpClientModule } from '@angular/common/http';
import { HistorialCompraService } from './services/historial-compra.service';







@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule, 
    AppRoutingModule,
    AboutModule,
    AuthModule,
    CartModule,
    CreateEventModule,
    Error404Module,
    EventsModule,
    HomeModule,
    ProfileUserModule,
    HttpClientModule
  ],
  providers: [HistorialCompraService],
  bootstrap: [AppComponent],
})
export class AppModule {}
