import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { EventsRoutingModule } from './events-routing.module';
import { EventItemComponent } from './components/event-item/event-item.component';
import { EventsComponent } from './pages/events/events.component';


@NgModule({
  declarations: [
    EventItemComponent,
    EventsComponent
  ],
  imports: [
    CommonModule,
    EventsRoutingModule
  ]
})
export class EventsModule { }
