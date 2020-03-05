<tr>
            <td>4:20<br>-<br>4:40</td>
            <td>{% with val='16 20 1 monday'|change%}
                {% if val == None %}
                {% with val='16 20 1 0'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 1 tuesday'|change%}
                {% if val == None %}
                {% with val='16 20 1 1'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 1 wednesday'|change%}
                {% if val == None %}
                {% with val='16 20 1 2'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 1 thursday'|change%}
                {% if val == None %}
                {% with val='16 20 1 3'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 1 friday'|change%}
                {% if val == None %}
                {% with val='16 20 1 4'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            
            <td>{% with val='16 20 2 monday'|change%}
                {% if val == None %}
                {% with val='16 20 2 0'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 2 tuesday'|change%}
                {% if val == None %}
                {% with val='16 20 2 1'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 2 wednesday'|change%}
                {% if val == None %}
                {% with val='16 20 2 2'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 2 thursday'|change%}
                {% if val == None %}
                {% with val='16 20 2 3'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 2 friday'|change%}
                {% if val == None %}
                {% with val='16 20 2 4'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 3 monday'|change%}
                {% if val == None %}
                {% with val='16 20 3 0'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 3 tuesday'|change%}
                {% if val == None %}
                {% with val='16 20 3 1'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 3 wednesday'|change%}
                {% if val == None %}
                {% with val='16 20 3 2'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 3 thursday'|change%}
                {% if val == None %}
                {% with val='16 20 3 3'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 3 friday'|change%}
                {% if val == None %}
                {% with val='16 20 3 4'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 4 monday'|change%}
                {% if val == None %}
                {% with val='16 20 4 0'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 4 tuesday'|change%}
                {% if val == None %}
                {% with val='16 20 4 1'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 4 wednesday'|change%}
                {% if val == None %}
                {% with val='16 20 4 2'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 4 thursday'|change%}
                {% if val == None %}
                {% with val='16 20 4 3'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
            <td>{% with val='16 20 4 friday'|change%}
                {% if val == None %}
                {% with val='16 20 4 4'|temp%}
                {% if val == None%}
                -
                {%else%}
                <a href="{% url 'temp-detail' val.id %}">

                    <div style="background-color:blue; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>

                </a>
                {%endif%}
                {% endwith %}
                {% else %}
                <a href="{% url 'student-detail' val.student.id %}">
                    {% if today == val.days_of_week %}
                    <div style="background-color:gray; color:white">
                        {{val.student.eng_name}}<br>
                        {{val.student.group}}
                    </div>
                    {%else%}
                    {{val.student.eng_name}}<br>
                    {{val.student.group}}
                    {%endif%}
                </a>
                {%endif%}
                {% endwith %}
            </td>
        </tr>