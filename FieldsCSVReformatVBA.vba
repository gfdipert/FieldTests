Sub FieldsCSVStep1()

lmax = ActiveSheet.Cells.SpecialCells(xlCellTypeLastCell).Column
For i1 = 1 To lmax

 If (Cells(1, i1).Value <> "availableToMarcom/__text" And Cells(1, i1).Value <> "contextualField/__text" And Cells(1, i1).Value <> "defaults/__text" And Cells(1, i1).Value <> "fieldType/__text" And Cells(1, i1).Value <> "name/__text" And Cells(1, i1).Value <> "otherDisplayOption/__text" And Cells(1, i1).Value <> "partnerEditable/__text" And Cells(1, i1).Value <> "toIgnorePartnerDefaults/__text" And Cells(1, i1).Value <> "values/__text") Then

        ActiveSheet.Columns(i1).EntireColumn.Delete
        i1 = i1 - 1
        lmax = lmax - 1
        If i1 >= lmax Then Exit Sub
 End If
Next i1

End Sub

Sub FieldsCSVStep2()

    Range("A1:I1").Select
    Selection.Find(What:="availableToMarcom/__text", After:=ActiveCell, LookIn _
        :=xlFormulas, LookAt:=xlWhole, SearchOrder:=xlByRows, SearchDirection:= _
        xlNext, MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""availableToMarcom/__text"",""Marcom"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Selection.Find(What:="contextualField/__text", After:=ActiveCell, LookIn _
        :=xlFormulas, LookAt:=xlWhole, SearchOrder:=xlByRows, SearchDirection:= _
        xlNext, MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""contextualField/__text"",""Contextual"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Selection.Find(What:="defaults/__text", After:=ActiveCell, LookIn:= _
        xlFormulas, LookAt:=xlWhole, SearchOrder:=xlByRows, SearchDirection:= _
        xlNext, MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""defaults/__text"",""Default Values"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Selection.Find(What:="fieldType/__text", After:=ActiveCell, LookIn:= _
        xlFormulas, LookAt:=xlWhole, SearchOrder:=xlByRows, SearchDirection:= _
        xlNext, MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""fieldType/__text"",""Field Type"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Selection.Find(What:="name/__text", After:=ActiveCell, LookIn:=xlFormulas _
        , LookAt:=xlWhole, SearchOrder:=xlByRows, SearchDirection:=xlNext, _
        MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""name/__text"",""Field Name"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Selection.Find(What:="otherDisplayOption/__text", After:=ActiveCell, _
        LookIn:=xlFormulas, LookAt:=xlWhole, SearchOrder:=xlByRows, _
        SearchDirection:=xlNext, MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""otherDisplayOption/__text"",""Other Personalization"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Selection.Find(What:="partnerEditable/__text", After:=ActiveCell, LookIn _
        :=xlFormulas, LookAt:=xlWhole, SearchOrder:=xlByRows, SearchDirection:= _
        xlNext, MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""partnerEditable/__text"",""Partner Editable"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Selection.Find(What:="toIgnorePartnerDefaults/__text", After:=ActiveCell, _
        LookIn:=xlFormulas, LookAt:=xlWhole, SearchOrder:=xlByRows, _
        SearchDirection:=xlNext, MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""toIgnorePartnerDefaults/__text"",""Skip Partner Defaulting"",1,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Cells.Find(What:="values/__text", After:=ActiveCell, LookIn:=xlFormulas, _
        LookAt:=xlPart, SearchOrder:=xlByRows, SearchDirection:=xlNext, _
        MatchCase:=False).Activate
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""values/__text"",""Values"",2,1,TRUE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    
    Dim arrColOrder As Variant, ndx As Integer
    Dim Found As Range, counter As Integer
    
    arrColOrder = Array("Field Name", "Field Type", "Partner Editable", "Contextual", "Other Personalization", "Marcom", "Skip Partner Defaulting", "Values", "Default Values")
    
    counter = 1
    
    Application.ScreenUpdating = False
    
    For ndx = LBound(arrColOrder) To UBound(arrColOrder)
    
        Set Found = Rows("1:1").Find(arrColOrder(ndx), LookIn:=xlValues, LookAt:=xlWhole, _
                          SearchOrder:=xlByColumns, SearchDirection:=xlNext, MatchCase:=False)
        
        If Not Found Is Nothing Then
            If Found.Column <> counter Then
                Found.EntireColumn.Cut
                Columns(counter).Insert Shift:=xlToRight
                Application.CutCopyMode = False
            End If
            counter = counter + 1
        End If
        
    Next ndx
    
    Application.ScreenUpdating = True

    Columns("A:I").Select
    ActiveSheet.ListObjects.Add(xlSrcRange, Range("$A:$I"), , xlYes).Name = _
        "Table1"
    Columns("A:I").Select
    ActiveSheet.ListObjects("Table1").TableStyle = "TableStyleLight2"
    Range("J12").Select
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""edit"",""simple text"",1,2,FALSE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    ExecuteExcel4Macro _
        "FORMULA.REPLACE(""content"",""contextual content"",1,2,FALSE,FALSE,,FALSE,FALSE,FALSE,FALSE)"
    Columns("A:A").EntireColumn.AutoFit
    Columns("B:B").EntireColumn.AutoFit
    Columns("H:I").Select
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlBottom
        .WrapText = True
        .Orientation = 0
        .AddIndent = False
        .ShrinkToFit = False
        .MergeCells = False
    End With
End Sub


