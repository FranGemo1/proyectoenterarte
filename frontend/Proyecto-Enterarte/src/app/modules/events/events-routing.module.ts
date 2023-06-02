import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EventsComponent } from './pages/events/events.component';
import { EventItemComponent } from './components/event-item/event-item.component';

const routes: Routes = [
  {path: '',
  component: EventsComponent
  },
  {
    path:"event-item/:id", 
    component: EventItemComponent, 
    pathMatch: "full"
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EventsRoutingModule { }
