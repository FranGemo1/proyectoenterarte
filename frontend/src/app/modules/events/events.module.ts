import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EventsRoutingModule } from './events-routing.module';
import { EventItemComponent } from './components/event-item/event-item.component';
import { EventsComponent } from './pages/events/events.component';
import { CategoryFilterPipe } from './pipes/category-filter.pipe';




@NgModule({
  declarations: [
    EventItemComponent,
    EventsComponent,
    CategoryFilterPipe
  ],
  imports: [
    CommonModule,
    EventsRoutingModule
  ]
})
export class EventsModule { }
