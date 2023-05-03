import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EventsComponent } from './components/events/events.component';
import { EventItemComponent } from './components/event-item/event-item.component';
import { CreateEventComponent } from './components/create-event/create-event.component';
import { AboutComponent } from './components/about/about.component';
import { ProfileUserComponent } from './components/profile-user/profile-user.component';
import { LoginComponent } from './components/login/login.component';
import { HomeComponent } from './components/home/home.component';
import { Error404Component } from './components/error404/error404.component';

const routes: Routes = [

  {path: 'home', component: HomeComponent},
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'events', component: EventsComponent, children:[
    {path: 'event', component: EventItemComponent}
  ]},
  {path: 'create-event', component: CreateEventComponent},
  {path: 'about', component: AboutComponent},
  {path: 'profile-user', component: ProfileUserComponent},
  {path: 'login', component: LoginComponent},
  {path:'**', component: Error404Component, pathMatch: "full"}  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
