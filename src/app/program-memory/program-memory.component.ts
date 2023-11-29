import { Component } from '@angular/core';
import { Byte } from './byte';
import { instruction } from '../instruction-register/instruction';
import { ProgramMemoryToInstructionService } from '../services/program-memory-to-instruction.service';

const BitsForAdresses = 11

@Component({
  selector: 'app-program-memory',
  templateUrl: './program-memory.component.html',
  styleUrls: ['./program-memory.component.scss']
})
export class ProgramMemoryComponent {
  instructionToAdd:instruction
  instructionCounter:number
  requestedAdress:number  //this string gets adress from PC, and the number is the index of the element in memory<Byte>[] array
  memory: Array<Byte> = new Array<Byte>()
  resultWord:instruction  //should be register so we can send this register directly to the instruction register component

  constructor(public ProgMemToInstReg: ProgramMemoryToInstructionService){
    this.instructionToAdd = new instruction('0000000000000000000000000000000')
    this.instructionCounter = 0
    this.requestedAdress = 0
    this.resultWord = new instruction('0000000000000000000000000000000')
    for(let i = 0; i < Math.pow(2,BitsForAdresses); i++ ){
      this.memory.push(new Byte())
    }
  }

  sendToInstructionRegister():void{
    this.ProgMemToInstReg.instruction = this.resultWord
  }

  resetMemory(){
  for(let i=0; i<Math.pow(2,BitsForAdresses); i = i+4){
    this.memory[i].isValid = true;
  }
  }

  getInstruction():void{
    let adress = this.requestedAdress
    let retrievedInstruction:string = ''
    retrievedInstruction = retrievedInstruction + this.memory[adress].Binary
    retrievedInstruction = retrievedInstruction + this.memory[adress+1].Binary
    retrievedInstruction = retrievedInstruction + this.memory[adress+2].Binary
    retrievedInstruction = retrievedInstruction + this.memory[adress+3].Binary
    this.resultWord = new instruction(retrievedInstruction)
  }

  insertInstruction(inst:instruction):boolean{ 
    for(let i=0; i<Math.pow(2,BitsForAdresses); i = i+4){
      if(this.memory[i].isValid == true){
        this.instructionCounter++
        this.memory[i].isValid = false
        this.memory[i].Decimal = inst.ConvertBinToInt(inst.GetByte(1))
        this.memory[i].Binary = inst.GetByte(1)
        this.memory[i+1].Decimal = inst.ConvertBinToInt(inst.GetByte(2))
        this.memory[i+1].Binary = inst.GetByte(2)
        this.memory[i+2].Decimal = inst.ConvertBinToInt(inst.GetByte(3))
        this.memory[i+2].Binary = inst.GetByte(3)
        this.memory[i+3].Decimal = inst.ConvertBinToInt(inst.GetByte(4))
        this.memory[i+3].Binary = inst.GetByte(4)
        return true
      }
    }
    return false
  }
    
}


