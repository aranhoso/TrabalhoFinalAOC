import { Injectable } from '@angular/core';
import { instruction } from '../instruction-register/instruction';

@Injectable({
  providedIn: 'root'
})
export class ProgramMemoryToInstructionService {

  instruction:instruction = new instruction('00000000000000000000000000000000')
  
  constructor() { }
}
