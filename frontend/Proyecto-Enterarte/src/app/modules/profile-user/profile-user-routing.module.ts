import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProfileUserComponent } from './pages/profile-user/profile-user.component';

const routes: Routes = [
  {path: '',
  component: ProfileUserComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProfileUserRoutingModule { }
