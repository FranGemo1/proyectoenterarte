import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CartInfo } from './cart-info.component';

describe('CartInfo', () => {
  let component: CartInfo;
  let fixture: ComponentFixture<CartInfo>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CartInfo ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CartInfo);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
