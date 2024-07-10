from django.shortcuts import render,redirect
from .models import emp
from .models import emp_os
from .models import emp_wfh
from .models import department
from .models import leave
from .models import project
from .models import takes
from django.http import HttpResponse
# Create your views here.

def all(request):
        return render(request,'empsalary.html,index.html,view.html,viewemp.html,viewempos.html,viewempwfh.html,viewdepartment.html,viewproject.html,viewleave.html,viewtakes.html,modify.html,modifyemp.html,modifyempos.html,modifyempwfh.html,modifydepartment.html,modifyproject.html,modifyleave.html,modifytakes.html,editemp.html,editempos.html,editempwfh.html,editdepartment.html,editproject.html,editleave.html,edittakes.html,insertemployee.html,insertempos.html,insertempwfh.html,insertproject.html,insertdept.html,insertleave.html,inserttakes.html')

def index(request):
        return render(request,'index.html')

def insert(request):
        return render(request,'insert.html')

def modify(request):
        return render(request,'modify.html')

def modifyemp(request):
        user = emp.objects.all()
        return render(request,'modifyemp.html',{'userdata':user})

def modifyempwfh(request):
        user = emp_wfh.objects.all()
        return render(request,'modifyempwfh.html',{'userdata':user})

def modifyempos(request):
        user = emp_os.objects.all()
        return render(request,'modifyempos.html',{'userdata':user})

def modifydepartment(request):
        user = department.objects.all()
        return render(request,'modifydepartment.html',{'userdata':user})

def modifyproject(request):
        user = project.objects.all()
        return render(request,'modifyproject.html',{'userdata':user})

def modifytakes(request):
        user = takes.objects.all()
        return render(request,'modifytakes.html',{'userdata':user})

def modifyleave(request):
        user = leave.objects.all()
        return render(request,'modifyleave.html',{'userdata':user})

def deleteemp(request, vid):
    us = emp.objects.get(id=vid)
    us.delete()
    return redirect("/modifyemp")

def deleteempos(request, vid):
    us = emp_os.objects.get(id=vid)
    us.delete()
    return redirect("/modifyempos")

def deleteempwfh(request, vid):
    us = emp_wfh.objects.get(id=vid)
    us.delete()
    return redirect("/modifyempwfh")

def deletedepartment(request, vid):
    us = department.objects.get(id=vid)
    us.delete()
    return redirect("/modifydepartment")

def deleteproject(request, vid):
    us = project.objects.get(id=vid)
    us.delete()
    return redirect("/modifyproject")

def deletetakes(request, vid):
    us = takes.objects.get(id=vid)
    us.delete()
    return redirect("/modifytakes")

def deleteleave(request, vid):
    us = leave.objects.get(id=vid)
    us.delete()
    return redirect("/modifyleave")

def editemp(request, vid):
    us = emp.objects.get(id=vid)
    return render(request,'editemp.html',{'emp':us})

def updateemp(request, vid):
    newname=request.POST['empname']
    newcont=request.POST['empcont']
    newadd=request.POST['empadd']
    newdesg=request.POST['empdesg']
    newdept=request.POST['empdeptid']
    deptid = department.objects.get(id=newdept)
    us = emp.objects.get(id = vid)
    us.emp_name=newname
    us.emp_contact_no=newcont
    us.emp_address=newadd
    us.emp_designation=newdesg
    us.dept=deptid
    us.save()
    return redirect("/modifyemp")

def editempos(request, vid):
    us = emp_os.objects.get(id=vid)
    return render(request,'editempos.html',{'emp_os':us})

def updateempos(request, vid):
    newempid=request.POST['empid']
    newsalary=request.POST['empsal']
    empid = emp.objects.get(id=newempid)
    us = emp_os.objects.get(id = vid)
    us.emp=empid
    us.os_salary=newsalary
    us.save()
    return redirect("/modifyempos")

def editempwfh(request, vid):
    us = emp_wfh.objects.get(id=vid)
    return render(request,'editempwfh.html',{'emp_wfh':us})

def updateempwfh(request, vid):
    newempid=request.POST['empid']
    newsalary=request.POST['empsal']
    empid = emp.objects.get(id=newempid)
    us = emp_wfh.objects.get(id = vid)
    us.emp=empid
    us.wfh_salary=newsalary
    us.save()
    return redirect("/modifyempwfh")


def editdepartment(request, vid):
    us = department.objects.get(id=vid)
    return render(request,'editdepartment.html',{'department':us})

def updatedepartment(request, vid):
    newname=request.POST['deptname']
    us = department.objects.get(id = vid)
    us.dept_name=newname
    us.save()
    return redirect("/modifydepartment")

def editproject(request, vid):
    us = project.objects.get(id=vid)
    return render(request,'editproject.html',{'project':us})

def updateproject(request, vid):
    newdesc=request.POST['pdesc']
    newdept=request.POST['deptid']
    deptid = department.objects.get(id=newdept)
    us = project.objects.get(id = vid)
    us.p_description=newdesc
    us.dept=deptid
    us.save()
    return redirect("/modifyproject")

def editleave(request, vid):
    us = leave.objects.get(id=vid)
    return render(request,'editleave.html',{'leave':us})

def updateleave(request, vid):
    newdesc=request.POST['ldesc']
    us = leave.objects.get(id = vid)
    us.l_description=newdesc
    us.save()
    return redirect("/modifyleave")

def edittakes(request, vid):
    us = takes.objects.get(id=vid)
    return render(request,'edittakes.html',{'takes':us})

def updatetakes(request, vid):
    newemp=request.POST['empid']
    newl=request.POST['lid']
    newtdate=request.POST['tdate']
    newretdate=request.POST['retdate']
    newavail=request.POST['avail']
    empid = emp.objects.get(id=newemp)
    lid = leave.objects.get(id=newl)
    us = takes.objects.get(id = vid)
    us.emp=empid
    us.l=lid
    us.t_date=newtdate
    us.t_retdate=newretdate
    us.l_available=newavail
    us.save()
    return redirect("/modifytakes")

def viewemp(request):
        user = emp.objects.all()
        return render(request,'viewemp.html',{'userdata':user})

def viewempos(request):
        user = emp_os.objects.all()
        return render(request,'viewempos.html',{'userdata':user})

def viewempwfh(request):
        user = emp_wfh.objects.all()
        return render(request,'viewempwfh.html',{'userdata':user})

def viewdepartment(request):
        user = department.objects.all()
        return render(request,'viewdepartment.html',{'userdata':user})

def viewproject(request):
        user = project.objects.all()
        return render(request,'viewproject.html',{'userdata':user})

def viewtakes(request):
        user = takes.objects.all()
        return render(request,'viewtakes.html',{'userdata':user})

def viewleave(request):
        user = leave.objects.all()
        return render(request,'viewleave.html',{'userdata':user})

def view(request):
        return render(request,'view.html')

def empsalary(request):
        return render(request,'empsalary.html')

def insertemployee(request):
        return render(request,'insertemployee.html')

def insertempos(request):
        return render(request,'insertempos.html')

def insertempwfh(request):
        return render(request,'insertempwfh.html')

def insertdept(request):
        return render(request,'insertdept.html')

def insertleave(request):
        return render(request,'insertleave.html')

def insertproject(request):
        return render(request,'insertproject.html')

def inserttakes(request):
        return render(request,'inserttakes.html')

def insertemp(request):
    vname = request.POST['name'];
    vcont = request.POST['cont'];
    vaddr = request.POST['add'];
    vdesig = request.POST['desg'];
    vdeptid = request.POST['deptid'];
    deptid = department.objects.get(id=vdeptid)
    us = emp(emp_name = vname, emp_contact_no = vcont, emp_address = vaddr, emp_designation = vdesig , dept = deptid);
    us.save();
    return render(request,'empsalary.html')

def insertinempos(request):
    veid = request.POST['eid'];
    vsal = request.POST['empsal'];
    empid = emp.objects.get(id=veid)
    us = emp_os(emp = empid, os_salary = vsal);
    us.save();
    return render(request,'index.html')

def insertinempwfh(request):
    veid = request.POST['eid'];
    vsal = request.POST['empsal'];
    empid = emp.objects.get(id=veid)
    us = emp_wfh(emp = empid, wfh_salary = vsal);
    us.save();
    return render(request,'index.html')

def insertindept(request):
    vname = request.POST['deptname'];
    us = department(dept_name = vname);
    us.save();
    return render(request,'index.html')

def insertinproject(request):
    vdesc = request.POST['desc'];
    vdid = request.POST['deptid']
    dept = department.objects.get(id=vdid)
    us = project(p_description = vdesc, dept = dept);
    us.save();
    return render(request,'index.html')

def insertinleave(request):
    vdesc = request.POST['desc'];
    us = leave(l_description = vdesc);
    us.save();
    return render(request,'index.html')

def insertintakes(request):
    veid = request.POST['eid'];
    vlid = request.POST['lid'];
    vtdate = request.POST['tdate'];
    vtretdate = request.POST['tretdate'];
    vavail = request.POST['avail'];
    empid = emp.objects.get(id=veid)
    lid = leave.objects.get(id=vlid)
    us = takes(emp = empid, l = lid, t_date = vtdate, t_retdate = vtretdate , l_available = vavail);
    us.save();
    return render(request,'index.html')
