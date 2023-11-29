import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterFileComponent } from './register-file/register-file.component';
import { ALUComponent } from './alu/alu.component';
import { InstructionRegisterComponent } from './instruction-register/instruction-register.component';
import { ProgramMemoryComponent } from './program-memory/program-memory.component';
import { ProgramCounterComponent } from './program-counter/program-counter.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterFileComponent,
    ALUComponent,
    InstructionRegisterComponent,
    ProgramMemoryComponent,
    ProgramCounterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
