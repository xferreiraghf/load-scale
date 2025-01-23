Dim fso, Fileout
Set fso = CreateObject("Scripting.FileSystemObject")
If Not fso.FileExists("C:/balanca/PesoBal.BAL") Then
    Set Fileout = fso.CreateTextFile("C:/balanca/PesoBal.BAL", True, True)
    Fileout.Write "Funcionando 100%"
    Fileout.Close
End If