from flask  import Flask,jsonify, request
from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema


Base.metadata.create_all(engine)

session = Session()

exams =session.query(Exam).all()

if len(exams) == 0:

    python_exam = Exam("SQLAlchemy Exam",'Test your knowledgment about SQLAlchemy','Joshua')

    session.add(python_exam)
    session.commit()
    session.close()


    exams= session.query(Exam).all()


    print('### Exams')

    for exam in exams:
        print(f'({exam.id}) {exam.title} - {exam.description} - {exam.last_updated_by}')

else :

    for exam in exams:
        print(f'({exam.id}) {exam.title} - {exam.description} - {exam.last_updated_by}')


app = Flask(__name__)


Base.metadata.create_all(engine)

@app.route('/exams')
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()

    schema = ExamSchema(many= True)
    exams =schema.dump(exam_objects)

    session.close()
    return jsonify(exams)


@app.route('/exams',methods =['POST'])
def add_exam() :
    posted_exam =ExamSchema(only=('title','description'))\
        .load(request.get_json())   
    
    print(posted_exam)
    
    exam = Exam(**posted_exam, created_by="HTTP POST Request")

    #persist exam
    session= Session()
    session.add(exam)
    session.commit()

    new_exam = ExamSchema().dump(exam)
    session.close()
    return jsonify(new_exam)

    

