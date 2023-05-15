import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProfileUserRoutingModule } from './profile-user-routing.module';
import { ProfileUserComponent } from './pages/profile-user/profile-user.component';


@NgModule({
  declarations: [
    ProfileUserComponent
  ],
  imports: [
    CommonModule,
    ProfileUserRoutingModule
  ]
})
export class ProfileUserModule { }
