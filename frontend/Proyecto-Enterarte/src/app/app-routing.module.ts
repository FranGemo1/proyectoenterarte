import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './modules/home/pages/home/home.component';

const routes: Routes = [

  {
    path: 'home', 
    component: HomeComponent
  },
  {
    path: 'events', 
    loadChildren: () =>
      import('./modules/events/events.module').then((m) => m.EventsModule)   
  },
  {
    path: 'create-event', 
    loadChildren: () =>
      import('./modules/create-event/create-event.module').then((m) => m.CreateEventModule)   
  },
  {
    path: 'about', 
    loadChildren: () =>
      import('./modules/about/about.module').then((m) => m.AboutModule)   
  },
  {
    path: 'profile-user', 
    loadChildren: () =>
      import('./modules/profile-user/profile-user.module').then((m) => m.ProfileUserModule)   
  },
  {
    path: 'login', 
    loadChildren: () =>
      import('./modules/auth/auth.module').then((m) => m.AuthModule)   
  },  
  {
    path: 'cart', 
    loadChildren: () =>
      import('./modules/cart/cart.module').then((m) => m.CartModule)   
  }, 
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },  
  {
    path:'**',  
    loadChildren: () =>
      import('./modules/error404/error404.module').then((m) => m.Error404Module)
  }  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
