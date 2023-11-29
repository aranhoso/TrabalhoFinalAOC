import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ALUComponent } from './alu.component';

describe('ALUComponent', () => {
  let component: ALUComponent;
  let fixture: ComponentFixture<ALUComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ALUComponent]
    });
    fixture = TestBed.createComponent(ALUComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
