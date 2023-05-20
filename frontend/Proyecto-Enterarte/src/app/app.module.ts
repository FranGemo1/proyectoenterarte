import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/header/header.component';
import { FooterComponent } from './shared/footer/footer.component';
import { EventsComponent } from './components/events/events.component';
import { EventItemComponent } from './components/event-item/event-item.component';
import { CreateEventComponent } from './components/create-event/create-event.component';
import { AboutComponent } from './components/about/about.component';
import { ProfileUserComponent } from './components/profile-user/profile-user.component';
import { HomeComponent } from './components/home/home.component';
import { Error404Component } from './components/error404/error404.component';
import { RegistroComponent } from './auth/registro/registro.component';
import { LoginComponent } from './components/login/login.component';
import { CommonModule } from '@angular/common';
import { HomeService } from './components/home/home.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    EventsComponent,
    EventItemComponent,
    CreateEventComponent,
    AboutComponent,
    ProfileUserComponent,
    LoginComponent,
    HomeComponent,
    Error404Component,
    RegistroComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, CommonModule],
  providers: [HomeService],
  bootstrap: [AppComponent],
})
export class AppModule {}
export class HomeModule {}
