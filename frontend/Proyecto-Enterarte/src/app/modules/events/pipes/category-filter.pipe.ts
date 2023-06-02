import { Pipe, PipeTransform } from '@angular/core';
import { Event } from '../interfaces/event';

@Pipe({
  name: 'categoryFilter'
})
export class CategoryFilterPipe implements PipeTransform {

  transform(events:Event[], category: string): any {
    if (!events || !category) {
      return events;
  }
   
    return events.filter (event => event.category==category)
}

}
