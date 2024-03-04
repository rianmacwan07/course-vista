import streamlit as st
from pages.enrollment import *
import webbrowser
class course_analysis:
    def button(self):
        btn = st.button("ENROLL NOW")
        if btn:
            webbrowser.open('http://localhost:8501/enrollment')
    def main_course(self):
        main_course = st.sidebar.selectbox('Courses',['Main','Specialization Course','Additional Course'],key=10)

        if main_course == 'Main':
            course_analysis.Courses(course_analysis)
        elif main_course == "Specialization Course":
            course_analysis.specilization_courses(course_analysis)
        elif main_course == "Additional Course": 
            course_analysis.additional_courses(course_analysis)
    def Courses(self):
        st.title("MAIN COURSES")
        courses = st.selectbox("select an option:",["Mechanical Engineering", "Electrical Engineering", "Computer Science", "Civil Engineering", "Chemical Engineering"],key=20)
        if courses== "Mechanical Engineering":
           st.subheader('''Mechanical engineers design and analyze mechanical systems and machinery.
            Benefits of Learning: Gain expertise in the design and manufacturing of various products and machines.
        Future Scope: Opportunities in industries like automotive, aerospace, and energy systems.''')
           st.image("mechanic.jpg")
           st.text("")
           st.text('''
A mechanical engineering course typically focuses on the principles and applications of mechanical systems, machinery, and structures. It is a diverse field that encompasses various disciplines such as mechanics, thermodynamics, materials science, and fluid dynamics.
Here's a general overview of what you might expect to study in a mechanical engineering course, along with some typical subjects:
Engineering Mechanics: This subject covers the fundamental principles of mechanics, including statics (study of forces in equilibrium) and dynamics (study of motion).
Mechanical Design: This involves the study of design principles, materials selection, and manufacturing processes for mechanical components and systems.
Thermodynamics: Thermodynamics deals with the study of energy transfer and conversion, particularly in relation to heat and work. Topics include laws of thermodynamics, power cycles, and refrigeration cycles.
Fluid Mechanics: Fluid mechanics explores the behavior of fluids (liquids and gases) and their applications in engineering systems. Topics include fluid statics, fluid dynamics, and flow measurement.
Heat Transfer: Heat transfer focuses on the mechanisms of heat transfer (conduction, convection, and radiation) and their applications in engineering design.
Materials Science and Engineering: This subject covers the properties, behavior, and selection of materials used in mechanical engineering applications, inuding metals, polymers, ceramics, and composites.
Mechatronics: Mechatronics integrates mechanical systems with electronics and computer control. Topics include sensors, actuators, control systems, and robotics.
Manufacturing Processes: This subject covers various manufacturing techniques such as machining, casting, welding, and additive manufacturing (3D printing).
Machine Dynamics and Vibrations: Machine dynamics deals with the analysis of mechanical systems in motion, including vibrations and stability analysis.
Engineering Mathematics: Mechanical engineering requires a strong foundation in mathematics, including calculus, differential equations, linear algebra, and numerical methods.
Engineering Drawing and CAD: Engineering drawing teaches the principles of technical drawing and CAD (Computer-Aided Design) software for designing mechanical components and assemblies.
Engineering Ethics and Professionalism: This subject addresses ethical issues and professional responsibilities in engineering practice.
These subjects provide a broad understanding of mechanical engineering principles and prepare students for a wide range of career opportunities in industries such as automotive, aerospace, energy, manufacturing, and robotics. Additionally, students often have opportunities for hands-on projects, internships, and research experiences to apply their knowledge in practical settings.''')

           course_analysis.button(course_analysis)

        
        elif courses== "Electrical Engineering":
            st.subheader('''  Electrical engineers work with electrical systems, electronics, and power generation.
             Benefits of Learning: Develop skills in electronics, power systems, and control systems.
        Future Scope: Growing demand for renewable energy and smart technologies''')
            st.image("EN-branch.png")
            st.text("")
            st.text('''Electrical engineering is another diverse field that deals with the study, design, and application of electrical systems and devices. Here's an overview of what you might expect to study in an electrical engineering course, along with some typical subjects:
Circuit Analysis: This subject focuses on the analysis of electrical circuits, including DC and AC circuits, network theorems, and transient analysis.
Electronics: Electronics covers the study of electronic components, devices, and circuits. Topics include semiconductor physics, diodes, transistors, amplifiers, and digital electronics.
Electromagnetic Theory: Electromagnetic theory deals with the fundamental principles of electromagnetism, including Maxwell's equations, electromagnetic waves, transmission lines, and antennas.
Signals and Systems: This subject explores the analysis and processing of signals in both time and frequency domains. Topics include Fourier analysis, Laplace transforms, and system response.
Power Systems: Power systems focus on the generation, transmission, and distribution of electrical power. Topics include power generation techniques, transformers, transmission lines, and power system stability.
Control Systems: Control systems deal with the analysis and design of systems that regulate the behavior of dynamic systems. Topics include feedback control, PID controllers, and stability analysis.
Digital Signal Processing (DSP): DSP involves the manipulation and analysis of digital signals using algorithms and digital processing techniques. Topics include discrete Fourier transforms, digital filters, and image processing.
Microelectronics and VLSI Design: Microelectronics covers the design and fabrication of integrated circuits (ICs) and microelectronic devices. Topics include CMOS technology, VLSI design methodologies, and semiconductor device modeling.
Renewable Energy Systems: This subject explores renewable energy sources such as solar, wind, and hydroelectric power systems. Topics include energy conversion techniques, grid integration, and sustainable energy policies.
Communication Systems: Communication systems focus on the transmission and reception of information over various channels. Topics include modulation techniques, digital communication principles, and wireless communication systems.
Power Electronics: Power electronics deals with the conversion and control of electrical power using electronic devices such as thyristors, MOSFETs, and IGBTs. Topics include power converters, motor drives, and renewable energy inverters.
Engineering Mathematics: Similar to mechanical engineering, electrical engineering requires a strong foundation in mathematics, including calculus, differential equations, linear algebra, and probability theory.
These subjects provide a comprehensive understanding of electrical engineering principles and prepare students for careers in industries such as electronics, telecommunications, power generation, automation, and renewable energy. Practical experience through lab work, projects, internships, and research opportunities is often integrated into the curriculum to enhance students' skills and prepare them for real-world applications.''')
            course_analysis.button(course_analysis)
        
        elif courses=="Computer Science":
            st.subheader('''Computer engineers design hardware and software systems, including computer networks.
             Benefits of Learning: Master programming, software development, and cybersecurity.
        Future Scope: Booming tech industry, with roles in software development, AI, and cybersecurity.''')
            st.image("comp.jpg")
            st.text("")
            st.text('''Computer engineering combines principles from both electrical engineering and computer science to design and develop hardware and software systems.
Here's an overview of what you might expect to study in a computer engineering course, along with some typical subjects:

Digital Logic and Computer Architecture: This subject covers the fundamentals of digital logic design, computer organization, and architecture. Topics include Boolean algebra, combinational and sequential logic circuits, CPU design, memory systems, and instruction set architecture.
Programming and Data Structures: Programming courses typically cover multiple programming languages (e.g., C, C++, Java) and focus on software development principles, algorithms, and data structures such as arrays, linked lists, stacks, queues, trees, and graphs.
Computer Networks: Computer networks focus on the principles and protocols governing communication between computers and devices. Topics include network architecture, protocols (e.g., TCP/IP, HTTP, DNS), routing algorithms, network security, and wireless communication.
Operating Systems: Operating systems cover the design and implementation of software systems that manage computer hardware and provide services to user applications. Topics include process management, memory management, file systems, and virtualization.
Embedded Systems: Embedded systems involve the design of computer systems embedded within larger devices or systems. Topics include microcontroller programming, real-time operating systems, sensor interfacing, and control systems.
Software Engineering: Software engineering focuses on software development methodologies, software design patterns, software testing, and project management techniques for developing reliable and maintainable software systems.
Computer Architecture and Design: This subject delves deeper into the design of modern computer systems, including pipelining, caching, parallel processing, and advanced CPU architectures.
Database Systems: Database systems cover the design, implementation, and management of databases to store and retrieve data efficiently. Topics include relational database design, SQL queries, transaction management, and database optimization.
Machine Learning and Artificial Intelligence: Machine learning and AI courses cover algorithms and techniques for building intelligent systems that can learn from data and make predictions or decisions. Topics include supervised and unsupervised learning, neural networks, deep learning, and natural language processing.
Computer Graphics and Visualization: Computer graphics courses focus on the principles and algorithms for rendering images and graphics on a computer screen. Topics include 2D and 3D graphics rendering, rasterization, ray tracing, and animation.
Cybersecurity: Cybersecurity courses cover techniques and strategies for protecting computer systems and networks from malicious attacks and threats. Topics include cryptography, network security protocols, penetration testing, and security policies.
Human-Computer Interaction: HCI courses explore the design and evaluation of user interfaces and interactive systems. Topics include usability principles, user experience design, interaction design, and user research methods.
                    These subjects provide a comprehensive understanding of computer engineering principles and prepare students for careers in industries such as software development, embedded systems, networking, cybersecurity, artificial intelligence, and computer graphics. Practical experience through projects, internships, and research opportunities is often integrated into the curriculum to enhance students' skills and prepare them for real-world applications.''')
            course_analysis.button(course_analysis)

        elif courses=="Civil Engineering":
            st.subheader('''Civil engineers design and maintain infrastructure such as buildings, bridges, roads, and dams.
             Benefits of Learning:Learn to create sustainable and safe structures, and contribute to urban development.
        Future Scope:High demand for infrastructure development worldwide, including transportation and environmental projects.''') 
            st.text("")
            st.image("civil.jpg")
            st.text('''Civil engineering is a broad field that encompasses the planning, design, construction, and maintenance of infrastructure and built environments. Here's an overview of what you might expect to study in a civil engineering course, along with some typical subjects:

Structural Engineering: Structural engineering focuses on the design and analysis of structures to ensure they can withstand loads and environmental factors. Topics include structural analysis, mechanics of materials, structural design (e.g., buildings, bridges, dams), and earthquake engineering.
Geotechnical Engineering: Geotechnical engineering deals with the behavior of soil and rock materials and their interaction with civil engineering structures. Topics include soil mechanics, foundation engineering, slope stability, and underground construction.
Transportation Engineering: Transportation engineering involves the planning, design, and operation of transportation systems, including roads, highways, railways, airports, and public transit. Topics include traffic engineering, transportation planning, pavement design, and sustainable transportation.
Environmental Engineering: Environmental engineering focuses on the protection and improvement of the natural environment through the design and implementation of engineering solutions. Topics include water and wastewater treatment, air quality management, solid waste management, and environmental impact assessment.
Hydraulic Engineering: Hydraulic engineering deals with the flow and conveyance of water, including open channel flow, pipe flow, hydraulic structures (e.g., dams, channels, culverts), and flood management.
Construction Engineering and Management: Construction engineering covers the planning, scheduling, and management of construction projects. Topics include construction materials and methods, project management techniques, cost estimation, and construction safety.
Surveying and Geomatics: Surveying involves the measurement and mapping of land features to support civil engineering projects. Topics include surveying techniques (e.g., total station, GPS), cadastral surveying, photogrammetry, and geographic information systems (GIS).
Materials Engineering: Materials engineering focuses on the properties, behavior, and selection of construction materials such as concrete, steel, wood, and asphalt. Topics include material testing, durability, sustainability, and construction material specifications.
Structural Dynamics and Earthquake Engineering: This subject explores the dynamic behavior of structures under various loading conditions, including seismic loading. Topics include structural dynamics, vibration analysis, and seismic design principles.
Urban Planning and Design: Urban planning involves the design and management of urban areas to ensure efficient use of space, transportation systems, and infrastructure. Topics include land use planning, zoning regulations, urban design principles, and sustainable urban development.
Risk and Resilience in Civil Engineering: This subject covers risk assessment, hazard mitigation, and resilience strategies to enhance the safety and reliability of civil engineering infrastructure.
Professional Practice and Ethics: Civil engineering ethics addresses the professional responsibilities and ethical considerations that engineers face in their practice, including safety, sustainability, and public welfare.
These subjects provide a comprehensive understanding of civil engineering principles and prepare students for careers in various sectors, including construction, transportation, environmental consulting, water resources management, and urban planning. Practical experience through internships, fieldwork, and design projects is often integrated into the curriculum to prepare students for real-world challenges in the civil engineering profession.''')
            course_analysis.button(course_analysis)
        
        elif courses=="Chemical Engineering":
            st.subheader('''Chemical engineers work with chemical processes and materials, often in manufacturing.
             Benefits of Learning:Learn to optimize chemical processes and design sustainable solutions.
        Future Scope:Opportunities in chemical, pharmaceutical, and environmental industries.''')
            st.image("chemical.jpg")
            st.text('''Chemical engineering is a branch of engineering that applies physical sciences (chemistry and physics) and life sciences (biology and biochemistry) to produce, transform, and transport materials and energy. Here's an overview of what you might expect to study in a chemical engineering course, along with some typical subjects:

Chemical Process Principles: This subject forms the foundation of chemical engineering and covers principles such as material and energy balances, thermodynamics, and reaction kinetics. Students learn how to design and analyze chemical processes.
Transport Phenomena: Transport phenomena involve the study of momentum, heat, and mass transfer in chemical engineering systems. Topics include fluid mechanics, heat transfer, and mass transfer principles applied to engineering processes.
Chemical Reaction Engineering: Chemical reaction engineering focuses on the design and optimization of chemical reactors and reaction systems. Topics include reactor design, reaction kinetics, catalysis, and multiphase reactors.
Unit Operations: Unit operations are fundamental steps in chemical engineering processes involving physical changes such as separation, mixing, filtration, and distillation. Topics include principles of unit operations, equipment design, and process optimization.
Process Control and Instrumentation: Process control involves the application of control theory and instrumentation to regulate and optimize chemical processes. Topics include feedback control systems, process dynamics, sensors, and control strategies.
Chemical Engineering Thermodynamics: This subject delves deeper into thermodynamic principles as applied to chemical engineering systems. Topics include phase equilibria, chemical potential, activity coefficients, and thermodynamic cycles.
Chemical Engineering Kinetics: Chemical kinetics focuses on the rates of chemical reactions and the factors that influence reaction rates. Topics include reaction mechanisms, rate laws, and methods for determining kinetic parameters.
Separation Processes: Separation processes involve the separation of components from mixtures in chemical processes. Topics include distillation, absorption, extraction, crystallization, membrane separation, and chromatography.
Process Design and Optimization: Process design involves the synthesis and optimization of chemical processes to achieve desired production goals while considering factors such as economics, safety, and environmental impact.
Bioprocess Engineering: Bioprocess engineering applies engineering principles to the design and optimization of processes involving biological materials, such as fermentation, enzyme kinetics, and bioreactor design.
Environmental Engineering: Environmental engineering focuses on the application of chemical engineering principles to address environmental challenges such as air and water pollution control, waste treatment, and sustainable processes.
Safety and Risk Management: Safety engineering involves identifying and mitigating risks associated with chemical processes to ensure the safety of workers, communities, and the environment.
These subjects provide a comprehensive understanding of chemical engineering principles and prepare students for careers in industries such as petroleum, pharmaceuticals, chemicals, materials, energy, food processing, and environmental engineering. Practical experience through internships, laboratory work, and design projects is often integrated into the curriculum to prepare students for real-world challenges in the chemical engineering profession.''')
            
            st.text("")
            course_analysis.button(course_analysis)
        return courses
    def specilization_courses(self):
        st.title("SPECIALIZATION COURSES")
        specialize=st.selectbox("select a course:",["Thermal Engineering",
"Mechatronics and Robotics",
"Automotive Engineering",
"Aerospace Engineering",
"Manufacturing Engineering",
"Materials Engineering",
"Mechanical Design Engineering",
"Energy Engineering",
"Biomechanical Engineering",
"Nuclear Engineering",
"Marine Engineering",
"Environmental Engineering",
"Renewable Energy Engineering"],key=30)
        
        if specialize == "Thermal Engineering":
            st.subheader('''Thermal engineers work with thermal systems and processes, vital in various industries including energy, HVAC, aerospace, and automotive.
            Benefits of Learning:Mastering thermal engineering enables optimization of energy systems and design of sustainable solutions for heating, cooling, and power generation.
        Future Scope:Opportunities abound in renewable energy development, smart HVAC technologies, electric vehicles, advanced materials for thermal management, and Industry 4.0 integration. Thermal engineers are also crucial in addressing environmental challenges through energy-efficient and sustainable solutions in various industries.''')
            st.image("thermal.jpg")
            st.text('''A "thermal course" typically refers to a course or program in thermal engineering, which focuses on the study, design, and optimization of systems involving thermal energy. Here's a description of such a course along with some typical subjects:

Description: A thermal engineering course aims to provide students with a comprehensive understanding of thermodynamics, heat transfer, fluid mechanics, and their applications in various engineering systems. Students learn to analyze, design, and optimize thermal systems for efficient energy conversion, utilization, and management. These systems include power plants, heating, ventilation, and air conditioning (HVAC) systems, refrigeration systems, renewable energy systems, and thermal management of electronic devices.

Typical Subjects:
Thermodynamics: Thermodynamics forms the foundation of thermal engineering, covering concepts such as energy, entropy, heat transfer, and the laws of thermodynamics.
Heat Transfer: Heat transfer deals with the mechanisms of heat transfer (conduction, convection, radiation) and their applications in engineering systems. Topics include steady-state and transient heat conduction, forced and natural convection, and heat exchanger design.
Fluid Mechanics: Fluid mechanics focuses on the behavior of fluids (liquids and gases) and their applications in thermal systems. Topics include fluid properties, fluid statics, fluid dynamics, and flow measurement.
Energy Systems Analysis: This subject involves the analysis of energy systems, including energy conversion processes, energy efficiency analysis, and modeling of energy systems using computational tools.
Thermal Systems Design: Thermal systems design covers the principles and methodologies for designing thermal systems such as power plants, HVAC systems, and refrigeration systems. Topics include component selection, system integration, and performance optimization.
Renewable Energy Technologies: This subject explores renewable energy sources such as solar, wind, geothermal, and biomass, focusing on their conversion technologies and integration into thermal systems.
Combustion Processes: Combustion processes involve the study of combustion fundamentals, combustion kinetics, and combustion chamber design for applications such as power generation and heating.
Refrigeration and Air Conditioning: Refrigeration and air conditioning systems cover the principles of refrigeration cycles, psychrometrics, HVAC system design, and energy-efficient cooling technologies.
Thermal System Modeling and Simulation: This subject involves the use of computational tools and software for modeling, simulating, and analyzing thermal systems to predict their performance and optimize their design.
Heat Exchanger Design: Heat exchanger design covers the principles of heat exchanger operation, types of heat exchangers, and design considerations for efficient heat transfer.
Thermal Management of Electronics: This subject focuses on thermal management techniques for electronic devices and systems to ensure optimal performance and reliability, including heat sink design, thermal interface materials, and cooling techniques.
Industrial Applications: Industrial applications of thermal engineering cover case studies and projects focused on real-world applications in industries such as power generation, manufacturing, aerospace, and automotive.

These subjects provide students with the knowledge and skills necessary to tackle challenges in thermal engineering and prepare them for careers in industries where thermal systems play a critical role in energy production, environmental sustainability, and technological innovation. Practical experience through laboratory experiments, projects, internships, and industry collaborations is often integrated into the curriculum to provide hands-on learning opportunities and enhance students' problem-solving abilities in thermal engineering.''')
        
        elif specialize == "Mechatronics and Robotics":
        
            st.subheader('''Mechatronics and robotics merge mechanical engineering, electrical engineering, computer science, and control systems to create intelligent systems and machines.
            Benefits of Learning: Learning mechatronics and robotics enables individuals to design smart systems, optimize automation processes, and develop innovative solutions across industries.
        Future Scope: Opportunities abound in manufacturing automation, healthcare robotics, autonomous vehicles, smart cities, consumer electronics, agriculture, space exploration, and environmental monitoring.''')
            st.image("robotics.jpg")
            st.text('''A mechatronics and robotics course combines mechanical engineering, electrical engineering, computer science, and control systems to equip students with the skills to design, build, and control intelligent systems and machines. Here's a description of such a course along with some typical subjects:

Description:
A mechatronics and robotics course aims to provide students with a multidisciplinary understanding of mechanical, electrical, and computer engineering principles, focusing on their integration for the design and development of smart systems and robotic devices. Students learn to apply concepts from mechanics, electronics, programming, and control theory to create innovative solutions for automation, manufacturing, healthcare, transportation, and other fields.

Typical Subjects:
Mechanical Engineering Fundamentals: This subject covers fundamental principles of mechanical engineering, including statics, dynamics, mechanics of materials, and machine design.
Electrical Engineering Fundamentals: Electrical engineering fundamentals cover topics such as circuit analysis, electronic devices, signals and systems, and electromechanical systems.
Computer Science and Programming: Students learn programming languages such as C/C++, Python, or MATLAB to develop software for controlling and interfacing with mechatronic and robotic systems.
Control Systems: Control systems theory focuses on the design and analysis of feedback control systems for regulating the behavior of dynamic systems. Topics include control system modeling, stability analysis, PID control, and state-space representation.
Robotics: Robotics subjects cover robot kinematics, dynamics, trajectory planning, and control algorithms for robot manipulators and mobile robots. Students learn about sensors and actuators used in robotics and study applications such as industrial robots, autonomous vehicles, and humanoid robots.
Sensors and Actuators: This subject covers the principles and characteristics of sensors and actuators used in mechatronic and robotic systems, including sensors for position, velocity, force, and vision, as well as actuators such as motors, pneumatic actuators, and servo systems.
Embedded Systems: Embedded systems subjects focus on the design and programming of microcontroller-based systems for real-time control and interfacing with sensors and actuators.
Mechatronic System Design: Mechatronic system design involves integrating mechanical, electrical, and software components to create mechatronic systems that meet specific performance requirements and constraints.
Robotics System Integration: This subject covers the integration of hardware and software components to build and program complete robotic systems, including sensor integration, data processing, and communication interfaces.
Machine Learning and Artificial Intelligence: Machine learning and AI subjects explore algorithms and techniques for enabling intelligent behavior in mechatronic and robotic systems, including computer vision, path planning, and decision-making algorithms.
Human-Robot Interaction: Human-robot interaction subjects focus on designing robots and systems that can interact with humans in various environments, including interface design, safety considerations, and social robotics.
Applications and Projects: Students work on hands-on projects and case studies to apply their knowledge and skills to real-world problems in areas such as automation, manufacturing, healthcare, transportation, and entertainment.

These subjects provide students with a solid foundation in mechatronics and robotics principles and prepare them for careers in industries such as manufacturing, automotive, aerospace, healthcare, and entertainment, where intelligent systems and robotic technologies are increasingly being utilized. Practical experience through laboratory experiments, projects, internships, and industry collaborations is often integrated into the curriculum to provide hands-on learning opportunities and enhance students' problem-solving abilities in mechatronics and robotics.''')
        st.text("")

        btn = st.button("ENROLL NOW",key=1)
        if btn:
               webbrowser.open('http://localhost:8501/enrollment')
        return specialize
    
    def additional_courses(self):
        st.title("ADDITIONAL COURSES")
        addtional = st.selectbox("select a course:",["Machine Learning",
        "Artificial Intelligence",
        "Automotive Engineering",
        "Engineering Ethics",
        "Engineering Economics",
        "Technical Writing",
        "Engineering Management",
        "Project Management",
        "Entrepreneurship",
        "Environmental Sustainability",
        "Renewable Energy Systems",
        "Cybersecurity for Engineers",
        "Data Science and Analytics",
        "Advanced Materials",
        "Robotics",
        "Nanotechnology"],key=40)

        btn = st.button("ENROLL NOW",key=2)
        if btn:
            webbrowser.open('http://localhost:8501/enrollment')

object = course_analysis()
object.main_course()
# object.Courses() 
#7974707672