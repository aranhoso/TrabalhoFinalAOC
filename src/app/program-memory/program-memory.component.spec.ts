import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProgramMemoryComponent } from './program-memory.component';

describe('ProgramMemoryComponent', () => {
  let component: ProgramMemoryComponent;
  let fixture: ComponentFixture<ProgramMemoryComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProgramMemoryComponent]
    });
    fixture = TestBed.createComponent(ProgramMemoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
