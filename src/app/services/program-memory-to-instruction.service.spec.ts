import { TestBed } from '@angular/core/testing';

import { ProgramMemoryToInstructionService } from './program-memory-to-instruction.service';

describe('ProgramMemoryToInstructionService', () => {
  let service: ProgramMemoryToInstructionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProgramMemoryToInstructionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
